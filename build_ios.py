from conans.client.conan_api import Conan
import platform
import os


conan_api, _, _ = Conan.factory()

conan_api.config_set("general.cmake_generator", "Xcode")
conan_api.update_profile("./profile/ios", "settings.os", "iOS")
conan_api.update_profile("./profile/ios", "settings.compiler", "apple-clang")
conan_api.update_profile("./profile/ios", "settings.compiler.version", "11.0")
conan_api.update_profile("./profile/ios", "settings.compiler.libcxx", "libc++")
conan_api.update_profile("./profile/ios", "settings.os.version", "9.0")
### just install pip every time?
CONAN_LOGIN_USERNAME = os.getenv('CONAN_LOGIN_USERNAME')
CONAN_PASSWORD = os.getenv('CONAN_PASSWORD')

conan_api.remote_add("bintray", f"https://api.bintray.com/conan/{CONAN_LOGIN_USERNAME}/test")
conan_api.authenticate(CONAN_LOGIN_USERNAME, CONAN_PASSWORD, "bintray")

conan_api.export("./ios_recipe", "dlib", "19.21", CONAN_LOGIN_USERNAME, "github_action")

conan_api.install("./build", build=["outdated"], profile_names=["./profile/ios"])
conan_api.upload("dlib", all_packages=True, confirm=True, remote_name="bintray")