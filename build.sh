conan user
conan profile new profile --detect
conan profile update settings.compiler.libcxx=libstdc++11 default
conan export recipe dlib/19.21@shuangliu1992/travis
cd build
conan install . --build=outdated
conan remote add bintray https://bintray.com/$CONAN_LOGIN_USERNAME
conan user -p $CONAN_PASSWORD -r bintray $CONAN_LOGIN_USERNAME
conan remote list
conan upload "*" --all --confirm -r=bintray