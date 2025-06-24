import asyncio
from viam.module.module import Module
try:
    from models.coDrive import Codrive
except ModuleNotFoundError:
    # when running as local module with run.sh
    from .models.coDrive import Codrive


if __name__ == '__main__':
    asyncio.run(Module.run_from_registry())
