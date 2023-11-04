IS_INSTALL=$1

if [ -z $IS_INSTALL ]; then
  echo 'Do you want to execute "bundle install"? [y/n]'
  read IS_INSTALL
fi

if [ "$IS_INSTALL" = "y" ]; then
  bundle install
fi

bundle exec jekyll build
python3 scripts/remove_space_href.py
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