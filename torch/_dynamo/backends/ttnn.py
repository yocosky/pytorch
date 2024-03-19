# This backend is maintained by Tenstorrent team.

from .registry import register_backend

try:
   import torch_ttnn  # type: ignore[import]
   _SUPPORT_TTNN = True
   register_backend(name="ttnn", compiler_fn=torch_ttnn.ttnn_backend)
except ImportError:
   _SUPPORT_TTNN = False


def has_ttnn():
   return _SUPPORT_TTNN

