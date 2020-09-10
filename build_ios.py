from conans.client.conan_api import Conan
import platform
import os


conan_api, _, _ = Conan.factory()

conan_api.create_profile("default", detect=True)
if platform.system() == "Linux":
    conan_api.update_profile("default", "settings.compiler.libcxx", "libstdc++11")
conan_api.config_set("general.cmake_generator", "Xcode")
conan_api.update_profile("default", "settings.os", "iOS")
conan_api.update_profile("default", "settings.os.version", "9.0")

CONAN_LOGIN_USERNAME = os.getenv('CONAN_LOGIN_USERNAME')
CONAN_PASSWORD = os.getenv('CONAN_PASSWORD')

conan_api.remote_add("bintray", f"https://api.bintray.com/conan/{CONAN_LOGIN_USERNAME}/test")
conan_api.authenticate(CONAN_LOGIN_USERNAME, CONAN_PASSWORD, "bintray")

conan_api.export("./ios_recipe", "dlib", "19.21", CONAN_LOGIN_USERNAME, "github_action")

conan_api.install("./build", build=["outdated"])
conan_api.upload("*", all_packages=True, confirm=True, remote_name="bintray")