# CLOMS

説明
CLMOS
[Comprehensive Life Management of Support ]

仕様
UNIPAとManabaを統合して、課題管理や体調管理表の提出を自動化するマクロを備えたシステム

作成内容
・課題のリマインド
・Google・Yahooカレンダーとの連携

【模式図】
CLMOS(フォルダ)
├── main.py(最初に起動させるファイル)
└── sub_code（フォルダ）
    ├── __init__
    ├── insert.py
    ├── get_report.py
    └──  get_event.py
