import TaskManager
import pytest

def test_add():
    tm = TaskManager.TaskManager()
    tm.add("Buy Milk")
    pending_task = 1
    assert pending_task == tm.pending_count()

def test_complete():
    tm = TaskManager.TaskManager()
    tm.add("Buy Chocolate")
    tm.complete(0)
    assert True == tm.tasks[0].done

def test_pending_count():
    tm = TaskManager.TaskManager()
    tm.add("Buy Milk")
    t1 = TaskManager.TaskManager()
    t1.add("Buy Biscuits")
    tm.complete(0)
    assert 1 == t1.pending_count()

def test_complete_exception():
    tm = TaskManager.TaskManager()
    tm.add("Buy Milk")
    tm.complete(5)
    assert tm.tasks[0].done == False

def test_save_load():
    tm = TaskManager.TaskManager()
    tm.add("Buy milk")
    tm.add("Buy tea")
    tm.complete(0)
    tm.save("testingList.txt")

    tm1 = TaskManager.TaskManager()
    tm1.load("testingList.txt")
    assert len(tm1.tasks) == 2; tm1.tasks[0].done == True; tm1.tasks[1].done == False