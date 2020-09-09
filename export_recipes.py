from conans.client.conan_api import Conan

conan_api, _, _ = Conan.factory()

conan_api.export("./recipe", "dlib", "19.21", "shuangliu1992", "travis")
