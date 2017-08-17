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


# Dependencies

This project works with Python >= 3.5. The test suite uses the [pytest](https://docs.pytest.org/en/latest/getting-started.html) module. 

# Your Task

The current implementation has a couple of bugs. There's a minimal set of tests that demonstrate some of the N bugs.

Modify the test suite in `test_server.py` until it exposes all the bugs. You will probably need to add some of your own test cases. Running the pytests should report the additional bugs.

You can run the tests by downloading or cloning this repository, then running the command `pytest` in the project directory.

Please package your solution as a tarball, including a short text file summarizing your changes.
