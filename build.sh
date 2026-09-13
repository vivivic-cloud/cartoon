#!/bin/sh
# 정적 배포용: index.html + images.json 생성 후 git push
cd "$(dirname "$0")"
cp app/index.html index.html
python3 -c "import json,os;print(json.dumps(sorted(f for f in os.listdir('.') if os.path.splitext(f)[1].lower() in {'.jpg','.jpeg','.png','.gif','.webp','.svg'} and not f.startswith('.')),ensure_ascii=False))" > images.json
git add -A && git commit -qm "update" && git push -q
