from database import Database1
from use_case import MyUseCase

use_case = MyUseCase(Database1())
use_case.insert_something()
use_case.search_something()
