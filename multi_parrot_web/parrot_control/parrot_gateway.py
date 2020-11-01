from parrot_control.ros import ROS

red_parrot_ids = [0, '0', 'RED', 'red']
blue_parrot_ids = [1, '1', 'BLUE', 'blue']


def get_parrot_std_id(parrot_id):
    if parrot_id in red_parrot_ids:
        return red_parrot_ids[0]
    elif parrot_id in blue_parrot_ids:
        return blue_parrot_ids[0]
    else:
        return None


_ros = ROS(2)


def ros():
    global _ros
    if _ros is None:
        _ros = ROS(2)
    return _ros


class ParrotGateway:

    def send_cmd(self, parrot_id, cmd):
        std_id = get_parrot_std_id(parrot_id)
        publishers = ros().get_parrot_publisher(std_id)

        publishers['cmd_name'].publish(str(cmd.name))
        if cmd.is_voice():
            publishers['voice_path'].publish(str(cmd.voice_relative_path))
        else:
            publishers['cmd_arg'].publish(str(cmd.arg))


parrot = ParrotGateway()
