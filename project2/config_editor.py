"""项目 2:JSON 配置文件读写器 - 读取、修改、验证、保存"""
import json
import os

CONFIG_FILE = "config.json"
VALID_THEMES = ["light", "dark", "auto"]
VALID_LANGUAGES = ["zh-CN", "en-US", "ja-JP"]
FONT_SIZE_MIN, FONT_SIZE_MAX = 8, 32

DEFAULT_CONFIG = {
    "theme": "light",
    "language": "zh-CN",
    "font_size": 14,
    "auto_save": True,
    "notifications": True,
}

def load_config():
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
        print(f"📝 未发现 {CONFIG_FILE},已创建默认配置")
        return dict(DEFAULT_CONFIG)
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

def validate(key, value):
    """返回 (是否合法, 处理后的值或错误信息)"""
    value = value.strip()
    if key == "theme":
        return (True, value) if value in VALID_THEMES else (False, f"必须是 {'/'.join(VALID_THEMES)} 之一")
    if key == "language":
        return (True, value) if value in VALID_LANGUAGES else (False, f"必须是 {'/'.join(VALID_LANGUAGES)} 之一")
    if key == "font_size":
        if not value.isdigit():
            return False, "必须是数字"
        size = int(value)
        if FONT_SIZE_MIN <= size <= FONT_SIZE_MAX:
            return True, size
        return False, f"必须在 {FONT_SIZE_MIN}-{FONT_SIZE_MAX} 之间"
    if key in ("auto_save", "notifications"):
        v = value.lower()
        if v in ("true", "1", "yes", "y"):
            return True, True
        if v in ("false", "0", "no", "n"):
            return True, False
        return False, "请输入 true 或 false"
    return False, "未知配置项"

def show_config(config):
    print("\n" + "=" * 44)
    print("            当前配置")
    print("=" * 44)
    for i, (k, v) in enumerate(config.items(), 1):
        print(f"  {i}. {k:<14} = {v}")
    print("=" * 44)

def main():
    config = load_config()
    keys = list(config.keys())
    while True:
        show_config(config)
        choice = input("\n输入要修改的项目编号(或 q 退出): ").strip()
        if choice.lower() == "q":
            print("✅ 配置已保存,再见!")
            break
        if not choice.isdigit() or not (1 <= int(choice) <= len(keys)):
            print("⚠️  请输入有效的编号")
            continue
        key = keys[int(choice) - 1]
        new_value = input(f"输入新的 {key} 值 (当前 = {config[key]}): ")
        ok, result = validate(key, new_value)
        if ok:
            config[key] = result
            save_config(config)
            print(f"✅ 已更新 {key} = {result}")
        else:
            print(f"⚠️  {result},未修改")

if __name__ == "__main__":
    main()
