conan profile new default --detect
conan export recipe dlib/19.21@$CONAN_LOGIN_USERNAME/travis
cd build
conan install . --build=outdated -s compiler.cppstd=17
conan remote add bintray https://api.bintray.com/conan/$CONAN_LOGIN_USERNAME/test 
conan user -p $CONAN_PASSWORD -r bintray $CONAN_LOGIN_USERNAME
conan remote list
conan upload "*" --all --confirm -r=bintray