# Server Gen Library

This toy library creates fictitious "servers" in a convenient manner for managing a fleet of role-specific hosts.

## API

To use the library:
```
import from server new_instance

new = new_instance(role, existing_hosts=None, attributes=None)
```

Where:
 - `role` is a string (e.g. `"web"`)
 - `existing_hosts` is a list of all existing instances of all roles.
 - `attributes` is a list of attributes to label the instance with.

 The returned value has the structure:
 ```
{
    "host_name": str
    "attributes": [...]
}
 ```

 Where, `host_name` will have the form `<role>-<#>.domain.com`.

 Note that `#` will be the lowest unused integer within the role.


## Dependencies

This project works with Python >= 3.5. The test suite uses the [pytest](https://docs.pytest.org/en/latest/getting-started.html) module. 

## Running the tests

You can run the tests by downloading or cloning this repository, installing the dependencies, then running the command `pytest` in the project directory.

## Your Task

The current implementation has a couple of bugs. There's a minimal set of tests that demonstrate some of the N bugs.

1. Create one text file, and in it, describe the currently exposed bugs.
2. In the same text file, describe the other bugs you found.
3. Modify `test_server.py` to expose the additional bugs. This should involve adding your own test cases as well as potentially modifying existing tests.
4. In the file where you described the bugs, describe the changes you made to the test suite and why you made them.

To be clear, _do not modify `server.py`_. Running `pytest` on your submission should result in failed test cases that expose all of the bugs in `server.py`


Please package your solution as a tarball, including the text file summarizing the bugs and your changes.
