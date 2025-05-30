import time
import hashlib
import json
import os
from datetime import datetime

# 加载配置
with open('config.json', 'r') as f:
    config = json.load(f)

def generate_live_url():
    """生成直播链接"""
    timestamp = int(time.time())
    
    # 动态生成密钥
    key_str = config["key_format"].format(t=timestamp)
    dynamic_key = hashlib.md5(key_str.encode()).hexdigest()
    
    return f"{config['base_url']}?t={timestamp}&k={dynamic_key}"

def update_m3u_file():
    """更新M3U文件"""
    new_url = generate_live_url()
    
    # 创建M3U内容
    m3u_content = f"#EXTM3U\n#EXTINF:-1,{config['channel_name']}\n{new_url}\n"
    
    # 写入文件
    with open('live.m3u', 'w', encoding='utf-8') as f:
        f.write(m3u_content)
    
    # 输出日志
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 直播链接已更新")
    print(f"新链接: {new_url}")
    
    return new_url

if __name__ == "__main__":
    update_m3u_file()