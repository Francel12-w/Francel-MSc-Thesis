from opentrons import protocol_api


metadata = {'protocolName': 'Characterisation of CoaB', 'author': 'Francel',
            'description': 'Adding Ppan and CTP = ',
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
    Ppan1 = source['A1']
    Ppan2 = source['A2']
    Ppan3 = source['A3']
    Ppan4 = source['A4']
    Ppan5 = source['B1']
    Ppan6 = source['B2']
    Blank_for_Ppan = source['B3']

    # Load sample to destinations:
    Ppan1_CTP1 = [destination['A4']]
    Ppan2_CTP1 = [destination['B4']]
    Ppan3_CTP1 = [destination['C4']]
    Ppan4_CTP1 = [destination['D4']]
    Ppan5_CTP1 = [destination['E4']]
    Ppan6_CTP1 = [destination['F4']]



    # First adding CTP
    # Well1 - CTP1:
    p300.pick_up_tip(tips['B9'])
    p300.flow_rate.aspirate = 50
    p300.flow_rate.dispense = 30
    p300.well_bottom_clearance.aspirate = 0.5
    p300.well_bottom_clearance.dispense = 0.5
    p300.transfer(30, Ppan1,  Ppan1_CTP1, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 50
    p300.drop_tip()

    p300.pick_up_tip(tips['B10'])
    p300.flow_rate.aspirate = 50
    p300.flow_rate.dispense = 30
    p300.well_bottom_clearance.aspirate = 0.5
    p300.well_bottom_clearance.dispense = 0.5
    p300.transfer(30, Ppan2,  Ppan2_CTP1, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 50
    p300.drop_tip()

    # Well3 :
    p300.pick_up_tip(tips['C1'])
    p300.flow_rate.aspirate = 50
    p300.flow_rate.dispense = 30
    p300.well_bottom_clearance.aspirate = 0.5
    p300.well_bottom_clearance.dispense = 0.5
    p300.transfer(30, Ppan3,  Ppan3_CTP1, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 50
    p300.drop_tip()

    # Well4 :
    p300.pick_up_tip(tips['C2'])
    p300.flow_rate.aspirate = 50
    p300.flow_rate.dispense = 30
    p300.well_bottom_clearance.aspirate = 0.5
    p300.well_bottom_clearance.dispense = 0.5
    p300.transfer(30, Ppan4,  Ppan4_CTP1, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 50
    p300.drop_tip()

    # Well5:
    p300.pick_up_tip(tips['C3'])
    p300.flow_rate.aspirate = 30
    p300.flow_rate.dispense = 30
    p300.well_bottom_clearance.aspirate = 0.5
    p300.well_bottom_clearance.dispense = 0.5
    p300.transfer(30, Ppan5,  Ppan5_CTP1, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 50
    p300.drop_tip()

    # Well6:
    p300.pick_up_tip(tips['C4'])
    p300.flow_rate.aspirate = 50
    p300.flow_rate.dispense = 30
    p300.well_bottom_clearance.aspirate = 0.5
    p300.well_bottom_clearance.dispense = 0.5
    p300.transfer(30, Ppan6,  Ppan6_CTP1, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 50
    p300.drop_tip()


