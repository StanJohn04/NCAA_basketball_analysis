# get all stats for all teams
def get_teamranking_stats(year_list,cat_list,merged_df):
    #import dependencies
    from splinter import Browser
    from bs4 import BeautifulSoup as bs
    import pandas as pd
    from datetime import datetime


    #track time
    now = datetime.now().strftime("%H:%M:%S")

    
    browser = Browser('chrome')
    url_count = 0
    print('Starting web scrape..')
    print(f'Current Time: {now}')
    cat_count = 0
    for cat in cat_list:
        
        print("-----------------")
        print(f"Category...{cat}")
        print("-----------------")
        
        year_count = 0
        for year in year_list:
            year_end = year - 1
            if year_count == 0:
                print(f'Starting with year...{year-1}')
                year_start = year-1
            else:
                print(f'Moving to year...{year-1}')
                
            url = f'https://www.teamrankings.com/ncaa-basketball/stat/{cat}?date={year}-04-05'
            
            try:
                browser.visit(url)
            except:
                print('Error occured on browser.visit()...')
                print(f'cat: {cat}')
                print(f'year: {year}')
                continue

            html = browser.html
            soup = bs(html, 'html.parser')
            
            try:
                table = pd.read_html(html)
            except:
                continue

            if year_count > 0:
                df2 = table[0]
                df2 = df2[['Team', f'{year-1}']]
                merged_df = merged_df.merge(df2, on = 'Team', how = 'outer')
            else:
                merged_df = table[0]
                merged_df = merged_df[['Team', f'{year-1}']]

            year_count += 1
            
        cat_count += 1
        try:
            merged_df.to_csv(f'../Resources/{cat}_{year_start}_{year_end}.csv')
        except:
            print(f'Error occured on to_csv()...data not saved for {cat}')
    browser.quit()
    
    now = datetime.now().strftime("%H:%M:%S")
    print("-----------------")
    print(f"End Time: {now}")
    print("-----------------")
    return f"Web scrape complete...data saved to csv"





def get_team_offense():
    browser = Browser('chrome')
    time.sleep(1)
    url = 'https://www.ncaa.com/stats/basketball-men/d1'
    browser.visit(url)
    time.sleep(1)
    # from homepage, click on scoring offense link
    browser.links.find_by_partial_text('Scoring Offense').click()
    time.sleep(1)
    counter = 2

    html = browser.html
    scoring_offense_soup = bs(html)

    pages_list = scoring_offense_soup.find_all('li', class_ = 'stats-pager__li')
    pages = len(pages_list) - 1

    for x in range(pages):
        #scrape table from first page then go to next page
        html = browser.html
        table = pd.read_html(html)

        if x == (pages -1):
            df2 = table[0]
            df = pd.concat([df,df2]).reset_index().drop(columns = 'index')
        elif x > 0:
            df2 = table[0]
            df = df.merge(df2, how = 'outer')
        else:
            df = table[0]

        try:
            browser.links.find_by_href(f"/stats/basketball-men/d1/current/team/145/p{counter}").click()
            time.sleep(1)
        except:
            print('Last page reached for team offense..')

        counter +=1
    browser.quit()
    return df



def get_all_stats(num_list, merged_df):
    browser = Browser('chrome')
    time.sleep(5)
    url_count = 0
    for num in num_list:
        if url_count == 0:
            print('Starting web scrape..')
        else:
            print('Moving to next stat category...')
        url = f'https://www.ncaa.com/stats/basketball-men/d1/current/team/{num}'
        browser.visit(url)
        time.sleep(2)
        
        div = browser.find_by_text('TEAM STATISTICS').first
        span = div.find_by_tag('span')
        
        page_header_text = span[0].text
        
        counter = 2

        html = browser.html
        soup = bs(html)
        
        pages_list = soup.find_all('li', class_ = 'stats-pager__li')
        pages = len(pages_list) - 1

        for x in range(pages):
            #scrape table from first page then go to next page
            html = browser.html
            table = pd.read_html(html)

            if x > 0:
                df2 = table[0]
                df = pd.concat([df,df2]).reset_index().drop(columns = 'index')
            else:
                df = table[0]

            try:
                browser.links.find_by_href(f"/stats/basketball-men/d1/current/team/{num}/p{counter}").click()
                time.sleep(2)
            except:
                print(f'Last page reached for {page_header_text}')

            counter +=1

        try:
            merged_df = pd.merge(merged_df,df, on = ['Team','GM']).drop(columns = ['Rank_x','Rank_y'])
        except:
            try:
                merged_df = pd.merge(merged_df,df, on = ['Team','GM']).drop(columns = 'Rank')
            except:
                print(f'**DEBUG**\n except clause on pd.merge.\n stat_category: {page_header_text}\n url_num:{num}')
                merged_df = pd.merge(merged_df, df,on = 'Team').drop(columns = 'Rank')
        
        url_count += 1  
    browser.quit()
    return merged_df

def merge_dfs(df1,df2,df3,df4,df5,df6):
    df_list = [df3,df4,df5]
    
    merged_df = pd.merge(df1,df2, on = ['Team','GM']).drop(columns = ['Rank_x','Rank_y'])
    
    for df in df_list:
        merged_df = pd.merge(merged_df, df,on = ['Team', "GM"]).drop(columns = 'Rank')
        
    merged_df = pd.merge(merged_df,df6, on = ['Team']).drop(columns = 'Rank')
    merged_df = merged_df.rename(columns = {'PPG_x':'PPG','PPG_y':'Bench_PPG'})
    
    return merged_df
