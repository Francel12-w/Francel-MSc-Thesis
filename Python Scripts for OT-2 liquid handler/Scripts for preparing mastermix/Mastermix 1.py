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
    # Preparing the mastermix:
    # MilliQ:
    p300.pick_up_tip(tips2['A1'])
    p300.flow_rate.aspirate = 210
    p300.flow_rate.dispense = 210
    p300.well_bottom_clearance.aspirate = 1
    p300.well_bottom_clearance.dispense = 2
    p300.transfer(107.1, MilliQ, Mastermix, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 210
    # Tris - Buffer:
    p300.flow_rate.aspirate = 150
    p300.flow_rate.dispense = 150
    p300.well_bottom_clearance.aspirate = 60 #falcon tube
    p300.well_bottom_clearance.dispense = 2
    p300.transfer(102, Tris_Buffer, Mastermix, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 150
    p300.drop_tip()
    # NADH :
    p300.pick_up_tip(tips2['A2'])
    p300.flow_rate.aspirate = 60
    p300.flow_rate.dispense = 60
    p300.well_bottom_clearance.aspirate = 1
    p300.well_bottom_clearance.dispense = 2
    p300.transfer(30.6, NADH, Mastermix, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 60
    p300.drop_tip()
    # DTT :
    p300.pick_up_tip(tips2['A3'])
    p300.flow_rate.aspirate = 50
    p300.flow_rate.dispense = 50
    p300.well_bottom_clearance.aspirate = 1
    p300.well_bottom_clearance.dispense = 3
    p300.transfer(20.4, DTT, Mastermix, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 50
    p300.drop_tip()

    # Cys :
    p300.pick_up_tip(tips2['A4'])
    p300.flow_rate.aspirate = 50
    p300.flow_rate.dispense = 50
    p300.well_bottom_clearance.aspirate = 1
    p300.well_bottom_clearance.dispense = 3
    p300.transfer(20.4, Cys, Mastermix, blow_out=True, blowout_location='destination well', new_tip='never')
    p300.flow_rate.blow_out = 50
    p300.drop_tip()

    # CoaBC :
    p300.pick_up_tip(tips2['A5'])
    p300.flow_rate.aspirate = 200
    p300.flow_rate.dispense = 200
    p300.well_bottom_clearance.aspirate = 1
    p300.well_bottom_clearance.dispense = 3
    p300.transfer(85, CoaBC, Mastermix, blow_out=True, blowout_location='destination well', new_tip='never',
                  mix_after=(3, 40))
    p300.flow_rate.blow_out = 200
    p300.drop_tip()







