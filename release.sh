bundle install
bundle exec jekyll build
python3 remove_space_href.py
cp CNAME _site/

git add .
git commit -m 'release'
git push origin main

cd _site/
git add .
git commit -m 'release'
git push origin master