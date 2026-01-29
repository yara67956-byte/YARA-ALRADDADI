def load_config(path: str = "config.json") -> Dict[str, Any]:
    # نفس نمط السلايد: with open + json.load :contentReference[oaicite:2]{index=2}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)