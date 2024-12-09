from opentrons import protocol_api


metadata = {'protocolName': 'Characterisation of CoaB', 'author': 'Francel',
            'description': 'Adding 170uL mastermix to 96-well plate',
            'apiLevel': '2.10'}


def run(protocol: protocol_api.ProtocolContext):
    # loading required labware
    tips = protocol.load_labware('opentrons_96_tiprack_300ul', 4)
    p300 = protocol.load_instrument('p300_single_gen2', mount='left', tip_racks=[tips])

    # loading in custom labware:
    source = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 8)
    destination = protocol.load_labware('nest_96_wellplate_200ul_flat', 2)

    # load the different mastermix samples:
    # Load samples:
    mastermix = source['A1']

    # Load sample to destinations:
    M1 = [destination['A3']]
    M2 = [destination['B3']]
    M3 = [destination['C3']]
    M4 = [destination['D3']]
    M5 = [destination['E3']]
    M6 = [destination['F3']]

    # Well1:
    p300.pick_up_tip(tips['B8'])
    p300.flow_rate.aspirate = 170
    p300.flow_rate.dispense = 170
    p300.well_bottom_clearance.aspirate = 6
    p300.well_bottom_clearance.dispense = 0.5
    p300.transfer(170, mastermix, M1, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 170

    # Well2 :
    p300.flow_rate.aspirate = 170
    p300.flow_rate.dispense = 170
    p300.well_bottom_clearance.aspirate = 6
    p300.well_bottom_clearance.dispense = 0.5
    p300.transfer(170, mastermix, M2, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 170

    # Well3 :
    p300.flow_rate.aspirate = 170
    p300.flow_rate.dispense = 170
    p300.well_bottom_clearance.aspirate = 4
    p300.well_bottom_clearance.dispense = 0.5
    p300.transfer(170, mastermix, M3, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 170

    # Well4 :
    p300.flow_rate.aspirate = 170
    p300.flow_rate.dispense = 170
    p300.well_bottom_clearance.aspirate = 4
    p300.well_bottom_clearance.dispense = 0.5
    p300.transfer(170, mastermix, M4, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 170

    # Well5 :
    p300.flow_rate.aspirate = 170
    p300.flow_rate.dispense = 170
    p300.well_bottom_clearance.aspirate = 3
    p300.well_bottom_clearance.dispense = 0.5
    p300.transfer(170, mastermix, M5, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 170

    # Well6 :
    p300.flow_rate.aspirate = 170
    p300.flow_rate.dispense = 170
    p300.well_bottom_clearance.aspirate = 1
    p300.well_bottom_clearance.dispense = 0.5
    p300.transfer(170, mastermix, M6, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 170



