bundle install
bundle exec jekyll build
python3 remove_space_href.py
cp CNAME _site/

git add .
git commit -m 'release'
git push bb main

cd _site
git init
git remote add origin https://github.com/dev-yakuza/dev-yakuza.github.io.git
git checkout -b master
git add .
git commit -m 'release'
git fetch
git push origin master -f