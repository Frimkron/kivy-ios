from toolchain import Recipe, shprint
from os.path import join
import sh


class LibSDL2ImageRecipe(Recipe):
    version = "2.0.0"
    url = "https://www.libsdl.org/projects/SDL_image/release/SDL2_image-{version}.tar.gz"
    library = "Xcode-iOS/build/Release-{arch.sdk}/libSDL2_image.a"
    include_dir = "SDL_image.h"
    depends = ["sdl2"]
    pbx_frameworks = ["CoreGraphics", "MobileCoreServices"]

    def build_arch(self, arch):
        shprint(sh.xcodebuild,
                "ONLY_ACTIVE_ARCH=NO",
                "ARCHS={}".format(arch.arch),
                "HEADER_SEARCH_PATHS={}".format(
                    join(self.ctx.include_dir, "common", "SDL2")),
                "-sdk", arch.sdk,
                "-project", "Xcode-iOS/SDL_image.xcodeproj",
                "-target", "libSDL_image",
                "-configuration", "Release")


recipe = LibSDL2ImageRecipe()

