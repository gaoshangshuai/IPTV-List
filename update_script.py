import re
import requests
import time
from urllib.parse import urlparse, parse_qs

def get_hebei_tv_url():
    """获取河北卫视直播源链接"""
    base_url = "https://tv.pull.hebtv.com/jishi/weishipindao.m3u8"
    # 生成时间戳和密钥（实际应用中可能需要从网页获取）
    timestamp = int(time.time())
    # 这里使用固定密钥（根据您提供的示例）
    key = "be4add580d3a62dbd555d3a09305c015"
    return f"{base_url}?t={timestamp}&k={key}"

def extract_m3u8_from_page(url):
    """从网页中提取m3u8链接"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # 使用正则表达式查找m3u8链接
        m3u8_pattern = r'(https?://[^\s]+?\.m3u8[^\s]*?)["\']'
        matches = re.findall(m3u8_pattern, response.text)
        
        if matches:
            # 返回找到的第一个m3u8链接
            return matches[0]
        return None
    except Exception as e:
        print(f"提取m3u8链接出错: {str(e)}")
        return None

if __name__ == "__main__":
    # 测试功能
    hebei_url = get_hebei_tv_url()
    print("河北卫视直播源:", hebei_url)
    
    # 示例：从其他网页提取m3u8
    # example_url = "http://example.com/live-tv-page"
    # extracted_url = extract_m3u8_from_page(example_url)
    # print("提取的直播源:", extracted_url)
