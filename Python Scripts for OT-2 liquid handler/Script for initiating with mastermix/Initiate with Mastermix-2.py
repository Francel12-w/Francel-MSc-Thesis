from opentrons import protocol_api


metadata = {'protocolName': 'Characterisation of CoaB', 'author': 'Francel',
            'description': 'Initiation of recation',
            'apiLevel': '2.10'}


def run(protocol: protocol_api.ProtocolContext):
    # loading required labware
    tips = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    p300 = protocol.load_instrument('p300_multi_gen2', mount='right', tip_racks=[tips])

    # loading in custom labware:
    plate = protocol.load_labware('nest_96_wellplate_200ul_flat', 2)

    mastermix = plate['A3']
    initiate = plate['A4']


    # Initiation of reaction:
    p300.pick_up_tip(tips['A2'])
    p300.flow_rate.aspirate = 120
    p300.flow_rate.dispense = 120
    p300.well_bottom_clearance.aspirate = 0.5
    p300.well_bottom_clearance.dispense = 1
    p300.transfer(120, mastermix, initiate, new_tip='never')
    p300.drop_tip()