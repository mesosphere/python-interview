

COMMON_DEFAULT_ATTRIBUTES = ["region:us-east-1", "owner:mesosphere"]


def new_instance(role, existing_hosts=None, attributes=None):
    # Generate the hostname
    host_name = "{}-{}.domain.com".format(role, _get_smallest_int(role, existing_hosts))

    return _create_new_server(host_name)

def _get_smallest_int(role, existing_hosts=None):
    if existing_hosts is None:
        return 1

    taken_ints = []
    for existing in existing_hosts:
        bits = existing.split(".")[0].split("-")
        if bits[0] == role:
            taken_ints.append(int(bits[1]))

    taken_ints.sort()
    for i, taken in enumerate(taken_ints):
        if i is len(taken_ints) - 1:
            print(i, taken, taken_ints)
            return taken + 1

        if taken_ints[i+1] - taken > 1:
            return taken + 1


def _create_new_server(host_name, attributes=[]):
    # All servers share the common defaults.
    attributes.extend(COMMON_DEFAULT_ATTRIBUTES)

    return {
        "host_name": host_name,
        "attributes": attributes
    }
