
from pymeasure.test import expected_protocol
from pymeasure.instruments.siglenttechnologies import SDS1072CML


def test_init():
    with expected_protocol(
            SDS1072CML,
            [],
    ):
        pass  # Verify the expected communication.


def test_waveform_setup_setter():
    with expected_protocol(
            SDS1072CML,
            [(b'WFSU SP,160,NP,5,FP,90', None)],
    ) as inst:
        inst.waveform_setup = {'sparsing': 160, 'number': 5, 'first': 90}


def test_waveform_setup_getter():
    with expected_protocol(
            SDS1072CML,
            [(b'WFSU?', b'WFSU SP,160,NP,5,FP,90,SN,0\n')],
    ) as inst:
        assert inst.waveform_setup == {'sparsing': 160, 'number': 5, 'first': 90}


def test_channel_1_get_waveform():
    with expected_protocol(
            SDS1072CML,
            [(b'C1:WF? ALL', b'C1:WF ALL,#9000000351WAVEDESC\x00\x00\x00\x00\x00\x00\x00\x00DSO\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00Z\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00SDS1072CML\x00\x00\x00\x00\x00\x00\xab\xcd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00P\x00\x00\xfeO\x00\x00\x00\x00\x00\x00\xffO\x00\x00Z\x00\x00\x00\xa0\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00o\x12\x03<\x00\x00\x00\x00\x00\x00\xfeB\x00\x00\x00\xc3\x08\x00\x01\x00\xbd7\x067\x00\x00\x00 \xe4\x11\xac\xbf\x00\x00\x00 \xe4\x11\xac\xbfV\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00S\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00_p\x890\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x14\x00\x04\x00\x00\x00\x80?\x06\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\n\n'),  # noqa: E501
             (b'C1:WF? DESC', b'C1:WF ALL,#9000000346WAVEDESC\x00\x00\x00\x00\x00\x00\x00\x00DSO\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00Z\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00SDS1072CML\x00\x00\x00\x00\x00\x00\xab\xcd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00P\x00\x00\xfeO\x00\x00\x00\x00\x00\x00\xffO\x00\x00Z\x00\x00\x00\xa0\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00o\x12\x03<\x00\x00\x00\x00\x00\x00\xfeB\x00\x00\x00\xc3\x08\x00\x01\x00\xbd7\x067\x00\x00\x00 \xe4\x11\xac\xbf\x00\x00\x00 \xe4\x11\xac\xbfV\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00S\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00_p\x890\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x14\x00\x04\x00\x00\x00\x80?\x06\x00\x00\x00\x00\x00\x80?\x00\x00\x00\x00\x00\x00\n'),  # noqa: E501
             (b'WFSU?', b'WFSU SP,160,NP,5,FP,90,SN,0\n')],
    ) as inst:
        assert inst.channel_1.get_waveform() == ([-0.05482399836182594, -0.05481599836184614, -0.05480799836186634, -0.05479999836188654, -0.054791998361906735], [0.0, 0.0, 0.0, 0.00800000037997961, 0.01600000075995922])  # noqa: E501
