from conans import ConanFile, CMake, tools

class DLIBConan(ConanFile):
    name = "dlib"
    version = "19.21"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Hello here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"

    # forfe a rebuild

    def init(self):
        self.source_path = f"{self.name}-{self.version}"

    def source(self):
        md5s = {}
        md5s["19.21"] = "a521a8a4d7aaba13465fbbc217bc4322"
        md5s["19.18"] = "3cf2a5b7a40fd61834dcb86c57638f38"
        tools.download(f"https://github.com/davisking/dlib/archive/v{self.version}.tar.gz", "src.tar.gz",
                       md5=md5s[self.version])

        tools.unzip("src.tar.gz")
        tools.replace_in_file(f"{self.source_path}/dlib/CMakeLists.txt", 'project(dlib)',
                              '''
                              project(dlib)
                              include(${CMAKE_BINARY_DIR}/../conanbuildinfo.cmake)
                              conan_basic_setup()
                              ''')

    def configure_cmake(self):
        # dlib install exclude build folder with regex pattern REGEX "${CMAKE_CURRENT_BINARY_DIR}" EXCLUDE)
        self.build_folder = self.build_folder + "/build"
        cmake = CMake(self)
        cmake.definitions['DLIB_USE_CUDA'] = "OFF"
        cmake.definitions['DLIB_ENABLE_STACK_TRACE'] = "OFF"
        cmake.definitions['DLIB_NO_GUI_SUPPORT'] = "ON"
        cmake.definitions['DLIB_USE_MKL_FFT'] = "OFF"
        cmake.definitions['DLIB_USE_BLAS'] = "OFF"
        cmake.definitions['DLIB_USE_LAPACK'] = "OFF"
        cmake.definitions['DLIB_PNG_SUPPORT'] = "OFF"
        cmake.definitions['DLIB_GIF_SUPPORT'] = "OFF"
        cmake.definitions['DLIB_JPEG_SUPPORT'] = "OFF"
        cmake.definitions['DLIB_ENABLE_ASSERTS'] = "OFF"
        cmake.definitions['DLIB_LINK_WITH_SQLITE3'] = "OFF"

        cmake.configure(source_folder=f"{self.source_path}/dlib")
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["dlib"]
