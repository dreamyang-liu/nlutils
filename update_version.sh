### Generate the version number
release_type=$1

version_mega_major=-1
version_major=-1
version_minor=-1

for i in $(cat release_info); do
    if [ $version_mega_major = -1 ]; then
        version_mega_major=$i
    elif [ $version_major = -1 ]; then
        version_major=$i
    elif [ $version_minor = -1 ]; then
        version_minor=$i
    fi
done

old_version=$version_mega_major.$version_major.$version_minor

if [ $release_type = 1 ]; then
    version_mega_major=$((version_mega_major+1))
    version_major=0
    version_minor=0
elif [ $release_type = 2 ]; then
    version_major=$((version_major+1))
    version_minor=0
elif [ $release_type = 3 ]; then
    version_minor=$((version_minor+1))
else
    echo "Invalid release type"
    exit 1
fi

new_version="$version_mega_major.$version_major.$version_minor"

echo "$version_mega_major $version_major $version_minor" > release_info

echo "Releasing $old_version -> $new_version"

### Build package and upload to PyPi
rm -rf dist
sed "s/@version/$new_version/" setup.py.template > setup.py