# SonaWrap
Reverse engineered python api wrapper for the sona academic studies systems mobile api

## How to use
Install with `pip install SonaWrap`

```python
from SonaWrap.Wrapper import SonaWrap
from config import credentials

# 1. AUTH
# Either give in username and password or existing token previously printed out to reuse authentication
sona = SonaWrap(username=credentials["username"], password=credentials["password"])
# sona = SonaWrap(token="b93ef8aed029418f871dc09c83283b67")

# 2. Usable routes
sona.test_connection()
sona.my_schedule()
sona.main_menu_info()
sona.study_page_info()

# one of the IDs from data of sona.study_page_info()
sona.study_info(1588)
```
