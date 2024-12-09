from opentrons import protocol_api

metadata = {'protocolName': 'Characterisation of CoaB', 'author': 'Francel',
            'description': 'Preparing mastermix',
            'apiLevel': '2.10'}


def run(protocol: protocol_api.ProtocolContext):
    # loading required labware
    tips2 = protocol.load_labware('opentrons_96_tiprack_300ul', 1)
    p300 = protocol.load_instrument('p300_single_gen2', mount='left', tip_racks=[tips2])

    # loading in custom labware:
    source_TRIS = protocol.load_labware('opentrons_10_tuberack_nest_4x50ml_6x15ml_conical', 7)
    source = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 5)

    # load the different mastermix samples:
    # Load CTP samples:
    Tris_Buffer = source_TRIS['A3']
    NADH = source['A1']
    DTT = source['A2']
    MilliQ = source['A3']
    Cys = source['B1']
    CoaBC = source['B2']
    Mastermix = source['B3']

    # Preparing the mastermix according to excel file:
    # MilliQ:
    p300.pick_up_tip(tips2['D8'])
    p300.flow_rate.aspirate = 210
    p300.flow_rate.dispense = 210
    p300.well_bottom_clearance.aspirate = 1
    p300.well_bottom_clearance.dispense = 2
    p300.transfer(153, MilliQ, Mastermix, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 210

    # Tris - Buffer:
    p300.flow_rate.aspirate = 160
    p300.flow_rate.dispense = 160
    p300.well_bottom_clearance.aspirate = 55  # falcon tube
    p300.well_bottom_clearance.dispense = 2
    p300.transfer(153, Tris_Buffer, Mastermix, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 160
    p300.drop_tip()

    # NADH :
    p300.pick_up_tip(tips2['D9'])
    p300.flow_rate.aspirate = 70
    p300.flow_rate.dispense = 70
    p300.well_bottom_clearance.aspirate = 1
    p300.well_bottom_clearance.dispense = 2
    p300.transfer(45.9, NADH, Mastermix, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 70
    p300.drop_tip()

    # DTT :
    p300.pick_up_tip(tips2['D10'])
    p300.flow_rate.aspirate = 50
    p300.flow_rate.dispense = 50
    p300.well_bottom_clearance.aspirate = 1
    p300.well_bottom_clearance.dispense = 3
    p300.transfer(30.6, DTT, Mastermix, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 50
    p300.drop_tip()

    # Cys :
    p300.pick_up_tip(tips2['D11'])
    p300.flow_rate.aspirate = 50
    p300.flow_rate.dispense = 50
    p300.well_bottom_clearance.aspirate = 1
    p300.well_bottom_clearance.dispense = 3
    p300.transfer(38.3, Cys, Mastermix, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 50
    p300.drop_tip()

    # CoaBC :
    p300.pick_up_tip(tips2['E1'])
    p300.flow_rate.aspirate = 250
    p300.flow_rate.dispense = 250
    p300.well_bottom_clearance.aspirate = 1
    p300.well_bottom_clearance.dispense = 3
    p300.transfer(191.3, CoaBC, Mastermix, blow_out=True, blowout_location='destination well', new_tip='never',
                  mix_after=(3, 40))
    p300.flow_rate.blow_out = 250
    p300.drop_tip()







