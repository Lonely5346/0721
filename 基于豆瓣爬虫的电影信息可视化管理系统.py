import requests
import json
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import font_manager
font_path = "C:/Windows/Fonts/simhei.ttf"  
font_prop = font_manager.FontProperties(fname=font_path)
rcParams['font.sans-serif'] = ['SimHei']  
rcParams['axes.unicode_minus'] = False   
cookies = {
    'll': '"118172"',
    'bid': '1g9KuH68SK4',
    '_pk_id.100001.4cf6': 'b0cd6adabb706ae6.1718802720.',
    '__yadk_uid': '7Fy28aQx1DCY4NnZHNsGL18fq4eCFizJ',
    '__utmc': '30149280',
    '__utmz': '30149280.1718802721.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    '__utmc': '223695111',
    '__utmz': '223695111.1718802721.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    '_vwo_uuid_v2': 'D816E9B77293C40EA8C8478097A9394E6|8963e2d5854837c41641bb0564b6793f',
    '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1718810576%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DI5UDdlLzyTcOQNcMLaeu6-ehnN7_hAH4R1JwYjyyLmFkXPGCnNdtD8MKfk52YKMgSTO_ecVUL9Drv0n-aGmR2q%26wd%3D%26eqid%3De79e93560000072c000000046672d91c%22%5D',
    '_pk_ses.100001.4cf6': '1',
    'ap_v': '0,6.0',
    '__utma': '30149280.23331474.1718455367.1718802721.1718810577.3',
    '__utma': '223695111.1593040718.1718802721.1718802721.1718810577.2',
    '__utmb': '223695111.0.10.1718810577',
    '__utmt': '1',
    '__utmb': '30149280.1.10.1718810577',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    # 'cookie': 'll="118172"; bid=1g9KuH68SK4; _pk_id.100001.4cf6=b0cd6adabb706ae6.1718802720.; __yadk_uid=7Fy28aQx1DCY4NnZHNsGL18fq4eCFizJ; __utmc=30149280; __utmz=30149280.1718802721.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; __utmz=223695111.1718802721.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=D816E9B77293C40EA8C8478097A9394E6|8963e2d5854837c41641bb0564b6793f; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1718810576%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DI5UDdlLzyTcOQNcMLaeu6-ehnN7_hAH4R1JwYjyyLmFkXPGCnNdtD8MKfk52YKMgSTO_ecVUL9Drv0n-aGmR2q%26wd%3D%26eqid%3De79e93560000072c000000046672d91c%22%5D; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.23331474.1718455367.1718802721.1718810577.3; __utma=223695111.1593040718.1718802721.1718802721.1718810577.2; __utmb=223695111.0.10.1718810577; __utmt=1; __utmb=30149280.1.10.1718810577',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://movie.douban.com/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'type': 'movie',
    'tag': '热门',
    'page_limit': '100',
    'page_start': '0',
}

response = requests.get('https://movie.douban.com/j/search_subjects', params=params, cookies=cookies, headers=headers)

movie_dict = response.json()
def display_all():
    print("\n所有电影信息:")
    titles = []
    rates = []
    for movie in movie_dict["subjects"]:
        print(f"标题: {movie['title']}, 评分: {movie['rate']}, 是否新片: {movie['is_new']}, 链接: {movie['url']}")
        titles.append(movie["title"])
        rates.append(float(movie["rate"]))

    N=15
    plt.bar(titles[:N], rates[:N], color='skyblue')
    plt.xlabel('电影标题')
    plt.ylabel('评分')
    plt.title('所有电影评分分布')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def filter_rating(min_rating):
    print(f"\n评分大于 {min_rating} 的电影：")
    filtered_movies = []
    for movie in movie_dict["subjects"]:
        if float(movie["rate"]) >= min_rating:
            print(f"标题: {movie['title']}, 评分: {movie['rate']}")
            filtered_movies.append(movie)

    if filtered_movies:
        titles = [movie["title"] for movie in filtered_movies]
        rates = [float(movie["rate"]) for movie in filtered_movies]
        N=15
        plt.bar(titles[:N], rates[:N], color='skyblue')
        plt.xlabel('电影标题')
        plt.ylabel('评分')
        plt.title(f'评分大于 {min_rating} 的电影')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("没有符合条件的电影。")

def filter_new():
    print("\n新片列表:")
    new_movies = [movie for movie in movie_dict["subjects"] if movie["is_new"]]
    for movie in new_movies:
        print(f"标题: {movie['title']}, 评分: {movie['rate']}")

    labels = ['新片', '非新片']
    sizes = [len(new_movies), len(movie_dict["subjects"]) - len(new_movies)]
    colors = ['gold', 'lightcoral']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('新片比例')
    plt.axis('equal')
    plt.show()

def search_title(keyword):
    print(f"\n搜索标题包含 '{keyword}' 的电影：")
    found_movies = [movie for movie in movie_dict["subjects"] if keyword.lower() in movie["title"].lower()]
    for movie in found_movies:
        print(f"标题: {movie['title']}, 评分: {movie['rate']}, 链接: {movie['url']}")

    plt.bar(['匹配电影', '其他电影'], [len(found_movies), len(movie_dict["subjects"]) - len(found_movies)], color=['blue', 'gray'])
    plt.ylabel('数量')
    plt.title(f"包含 '{keyword}' 的电影数量")
    plt.show()
my_favorites = []
def add_to_favorites(movie_title):
    """将电影添加到收藏列表"""
    for movie in movie_dict["subjects"]:
        if movie["title"] == movie_title:
            my_favorites.append(movie)
            print(f"电影《{movie_title}》已添加到收藏！")
            return
    print(f"未找到电影《{movie_title}》，无法添加到收藏。")

def view_favorites():
    """查看收藏的电影"""
    if not my_favorites:
        print("\n收藏列表为空!")
        return

    print("\n我的收藏:")
    titles = []
    rates = []
    for movie in my_favorites:
        print(f"标题: {movie['title']}, 评分: {movie['rate']}, 是否新片: {movie['is_new']}, 链接: {movie['url']}")
        titles.append(movie["title"])
        rates.append(float(movie["rate"]))

    N = 15
    plt.bar(titles[:N], rates[:N], color='orange')
    plt.xlabel('电影标题')
    plt.ylabel('评分')
    plt.title('我的收藏电影评分分布')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    print("''''''''''''''''''''''''''''''''''''''''''''")
    print("欢迎使用(豆瓣)电影信息管理系统V1.1")
    print("注意:所有电影信息均来自豆瓣API,数据仅供参考.")
    print("''''''''''''''''''''''''''''''''''''''''''''")
    while True:
        print("\n电影信息管理系统功能列表:")
        print("1. 显示所有电影")
        print("2. 按评分筛选电影")
        print("3. 显示新片")
        print("4. 搜索电影标题")
        print("5. 添加电影到收藏")
        print("6. 查看我的收藏")
        print("7. 退出")
        choice = input("请选择操作：")

        if choice == "1":
            display_all()
        elif choice == "2":
            min_rating = float(input("请输入最低评分："))
            filter_rating(min_rating)
        elif choice == "3":
            filter_new()
        elif choice == "4":
            keyword = input("请输入搜索关键词：")
            search_title(keyword)
        elif choice == "5":
            movie_title = input("请输入要收藏的电影标题：")
            add_to_favorites(movie_title)
        elif choice == "6":
            view_favorites()
        elif choice == "7":
            print("退出系统。")
            break
        else:
            print("无效选择，请重试。")

main()
