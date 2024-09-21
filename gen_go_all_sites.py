import os
import json


def generate_remote_urls():
    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # sites 目录路径
    sites_dir = os.path.join(script_dir, "./go/sites")
    
    # 初始化数据结构
    data_cdn = {"commons": [], "sites": []}
    data_github = {"commons": [], "sites": []}

    # 遍历 commons 目录下的所有文件
    commons_dir = os.path.join(script_dir, "./go/commons")
    for filename in os.listdir(commons_dir):
        if filename.endswith(".json"):
            remote_url_cdn = "https://cdn.jsdelivr.net/gh/mantou568/pre-dessert-sites@main/go/commons/" + filename
            remote_url_github = "https://raw.githubusercontent.com/mantou568/pre-dessert-sites/main/go/commons/" + filename
            data_cdn["commons"].append(remote_url_cdn)
            data_github["commons"].append(remote_url_github)

    # 遍历 sites 目录下的所有文件
    for filename in os.listdir(sites_dir):
        if filename.endswith(".json"):
            remote_url_cdn = "https://cdn.jsdelivr.net/gh/mantou568/pre-dessert-sites@main/go/sites/" + filename
            remote_url_github = "https://raw.githubusercontent.com/mantou568/pre-dessert-sites/main/go/sites/" + filename
            data_cdn["sites"].append(remote_url_cdn)
            data_github["sites"].append(remote_url_github)

    # 写入到 JSON 文件
    with open(os.path.join(script_dir, "all_go_sites_cdn.json"), "w") as f:
        json.dump(data_cdn, f, indent=4)
    
    with open(os.path.join(script_dir, "all_go_sites_github.json"), "w") as f:
        json.dump(data_github, f, indent=4)

    print("JSON 文件生成完成")


if __name__ == "__main__":
    generate_remote_urls()