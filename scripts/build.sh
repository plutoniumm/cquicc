rm -rf build;
bunx vite build;
touch build/.nojekyll;
touch build/CNAME;
echo "cquicc.manav.ch" > build/CNAME;