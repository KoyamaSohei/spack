# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAwscrt(PythonPackage):
    """Python 3 bindings for the AWS Common Runtime."""

    homepage = "https://docs.aws.amazon.com/sdkref/latest/guide/common-runtime.html"
    pypi = "awscrt/awscrt-0.16.16.tar.gz"

    maintainers("climbfuji")

    version("0.16.16", sha256="13075df2c1d7942fe22327b6483274517ee0f6ae765c4e6b6ae9ef5b4c43a827")

    depends_on("py-setuptools", type=("build"))
