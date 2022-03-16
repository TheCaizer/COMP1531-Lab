'''
Tests for the core functionality of the helpr application
Also need to change the test to keep track of the number of times
people are recevied help
'''
import pytest
# Don't change this import line below. If your tests are black-box tests then
# you don't require any more functions from the module than these
from helpr import make_request, queue, remaining, help, resolve, cancel, revert, reprioritise, end

def test_sanity():
    '''
    A simple sanity test of the system.
    '''
    # DO NOT CHANGE THIS TEST! If you feel you have to change this test then
    # your functions have not been implemented correctly.
    student1 = "z1234567"
    description1 = "I don't understand how 'global' works in python"
    student2 = "z7654321"
    description2 = "What's the difference between iterator and iterable?"

    # Queue is initially empty
    assert queue() == []

    # Student 1 makes a request
    make_request(student1, description1)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    assert remaining(student1) == 0

    # Student 2 makes a request
    make_request(student2, description2)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"},
                       {"zid": student2, "description": description2, "status": "waiting"}]
    assert remaining(student1) == 0
    assert remaining(student2) == 1

    # Student 1 gets help
    help(student1)
    assert queue() == [{"zid": student1, "description": description1, "status": "receiving"},
                       {"zid": student2, "description": description2, "status": "waiting"}]
    # Student 2 is now the only student "waiting" in the queue, so they have no
    # one remaining in front of them
    assert remaining(student2) == 0

    # Student 1 has their problem resolved
    resolve(student1)
    # Only student 2 is left in the queue
    assert queue() == [{"zid": student2, "description": description2, "status": "waiting"}]

    # Student is helped and their problem is resolved
    help(student2)
    resolve(student2)
    assert queue() ==[]

    # End the session
    end()

def test_make_request_error():
    '''test the value errorwhen empty string and when there is already a request'''
    make_request('z1234567', 'I cant code')
    with pytest.raises(ValueError):
        make_request('z111111', '')
    with pytest.raises(ValueError):
        make_request('z111111', ' ')
    with pytest.raises(KeyError):
        make_request('z1234567', 'I still cant code')
    end()

def test_make_request_normal():
    '''test that the make request adds to the queue'''
    student1 = 'z1234567'
    description1 = 'Hello'
    student2 = 'z1234568'
    description2 = 'Help me'
    assert queue() == []
    make_request(student1, description1)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    make_request(student2, description2)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"},
                       {"zid": student2, "description": description2, "status": "waiting"}]
    end()

def test_queue():
    '''test the queue returns normally'''
    assert queue() == []
    make_request('z1234567', 'Hello')
    assert queue() == [{"zid": 'z1234567', "description": 'Hello', "status": "waiting"}]
    #test the queue is adding to the end
    make_request('z7654321', 'Help me')
    assert queue() == [{"zid": 'z1234567', "description": 'Hello', "status": "waiting"},
                       {"zid": 'z7654321', "description": 'Help me', "status": "waiting"}]
    end()

def test_remaining_normal():
    '''test the remaing is returning the right number and is greater than one'''
    student1 = "z1234567"
    description1 = "Hello"
    student2 = "z7654321"
    description2 = "Help me"
    assert queue() == []
    make_request(student1, description1)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    assert remaining(student1) >= 0
    assert remaining(student1) == 0
    make_request(student2, description2)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"},
                       {"zid": student2, "description": description2, "status": "waiting"}]
    assert remaining(student1) == 0
    assert remaining(student2) >= 0
    assert remaining(student2) == 1
    help(student1)
    assert queue() == [{"zid": student1, "description": description1, "status": "receiving"},
                       {"zid": student2, "description": description2, "status": "waiting"}]
    assert remaining(student2) == 0
    end()

def test_remaining_error():
    '''test the Key Error Works'''
    #assume key error raise when the zid is not in the queue
    with pytest.raises(KeyError):
        remaining('z1234567')
    student1 = "z1234567"
    description1 = "Hello"
    assert queue() == []
    make_request(student1, description1)
    #change to recieveing help
    help(student1)
    with pytest.raises(KeyError):
        remaining('z1234567')
    end()
    
def test_help_normal():
    '''test the help function changes the zid of he student status to waiting'''
    student1 = 'z1234567'
    description1 = 'Hello'
    #make student
    make_request(student1, description1)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    #help student to change status to recieveing 
    help(student1)
    assert queue() == [{"zid": student1, "description": description1, "status": "receiving"}]
    que = queue()
    assert que[0]['status'] == "receiving"
    end()

def test_help_error():
    '''test the key error'''
    student1 = 'z1234567'
    description1 = 'Hello'
    #assume key error is raised when there is no student with zid in queue
    with pytest.raises(KeyError):
        help(student1)
    #make student
    make_request(student1, description1)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    #help student to change status to recieveing 
    help(student1)
    assert queue() == [{"zid": student1, "description": description1, "status": "receiving"}]
    #see for keyerror if student is not waiting
    with pytest.raises(KeyError):
        help(student1)
    end()

def test_resolve_normal():
    '''test that the resolve function removes the student from the queue'''
    student1 = 'z1234567'
    description1 = 'Hello'
    #make student
    make_request(student1, description1)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    #help student to change status to recieveing 
    help(student1)
    assert queue() == [{"zid": student1, "description": description1, "status": "receiving"}]
    resolve(student1)
    assert queue() == []
    end()

def test_resolve_error():
    '''test the keyerror when the student is not recieveing help'''
    student1 = 'z1234567'
    description1 = 'Hello'
    #assume key error is raised when there is no student with zid in queue
    with pytest.raises(KeyError):
        resolve(student1)
    #make student
    make_request(student1, description1)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    #make sure the key is raised when the student is still waiting and not helped
    with pytest.raises(KeyError):
        resolve(student1)
    end()

def test_cancel_normal():
    '''test that cancel works fine'''
    student1 = 'z1234567'
    description1 = 'Hello'
    student2 = 'z7654321'
    description2 = 'Help me'
    #make student
    make_request(student1, description1)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    make_request(student2, description2)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"},
                       {"zid": student2, "description": description2, "status": "waiting"}]
    cancel(student1)
    assert queue() == [{"zid": student2, "description": description2, "status": "waiting"}]
    end()

def test_cancel_error():
    '''test the errors for cancel function'''
    student1 = 'z1234567'
    description1 = 'Hello'
    #assume key error is raised when there is no student with zid in queue
    with pytest.raises(KeyError):
        cancel(student1)
    #make student
    make_request(student1, description1)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    help(student1)
    assert queue() == [{"zid": student1, "description": description1, "status": "receiving"}]
    #make sure the key is raised when the student is still being helped
    with pytest.raises(KeyError):
        cancel(student1)
    end()

def test_revert_normal():
    '''test that revert works normally'''
    student1 = 'z1234567'
    description1 = 'Hello'
    student2 = 'z7654321'
    description2 = 'Help me'
    #make student
    make_request(student1, description1)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    make_request(student2, description2)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"},
                       {"zid": student2, "description": description2, "status": "waiting"}]
    help(student1)
    assert queue() == [{"zid": student1, "description": description1, "status": "receiving"},
                       {"zid": student2, "description": description2, "status": "waiting"}]
    revert(student1)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"},
                       {"zid": student2, "description": description2, "status": "waiting"}]
    end()

def test_revert_error():
    '''test the errors in revert''' 
    student1 = 'z1234567'
    description1 = 'Hello'
    #assume key error is raised when there is no student with zid in queue
    with pytest.raises(KeyError):
        revert(student1)
    #make student
    make_request(student1, description1)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    #make sure the key is raised when the student is still waiting and not helped
    with pytest.raises(KeyError):
        revert(student1)
    end()

def test_end():
    '''test end removes all the requests'''
    student1 = 'z1234567'
    description1 = 'Hello'
    student2 = 'z7654321'
    description2 = 'Help me'
    student3 = 'z0987654'
    description3 = 'coding problems'
    #make student
    make_request(student1, description1)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    make_request(student2, description2)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"},
                       {"zid": student2, "description": description2, "status": "waiting"}]
    make_request(student3, description3)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"},
                       {"zid": student2, "description": description2, "status": "waiting"},
                       {"zid": student3, "description": description3, "status": "waiting"}]
    end()
    assert queue() == []
    end()

def test_reprioritise_normal():
    '''test that repriotitise works normally'''
    student1 = 'z1234567'
    description1 = 'Hello'
    student2 = 'z7654321'
    description2 = 'Help me'
    student3 = 'z0987654'
    description3 = 'coding problems'
        #make student
    make_request(student1, description1)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"}]
    make_request(student2, description2)
    assert queue() == [{"zid": student1, "description": description1, "status": "waiting"},
                       {"zid": student2, "description": description2, "status": "waiting"}]
    help(student1)
    help(student2)
    resolve(student1)
    resolve(student2)
    make_request(student1, description1)
    help(student1)
    resolve(student1)
    make_request(student2, description2)
    make_request(student1, description1)
    make_request(student3, description3)
    assert queue() == [{"zid": student2, "description": description2, "status": "waiting"},
                       {"zid": student1, "description": description1, "status": "waiting"},
                       {"zid": student3, "description": description3, "status": "waiting"}]
    reprioritise()
    assert queue() == [{"zid": student2, "description": description2, "status": "waiting"},
                       {"zid": student1, "description": description1, "status": "waiting"},
                       {"zid": student3, "description": description3, "status": "waiting"}]
    end()
