class QData:
    
    def __init__(self, question, answer=None):

        self.question = question
        self.answer = answer
    
tellme = [

    QData (
        'Tell me how you’d check that the brakes are working before starting a journey.',
        'Brakes should not feel spongy or slack. Brakes should be tested as you set off. Vehicle should not pull to one side.'
    ),

    QData (
        'Tell me where you’d find the information for the recommended tyre pressures for this car and how tyre pressures should be checked.',
        'Manufacturer’s guide, use a reliable pressure gauge, check and adjust pressures when tyres are cold, don’t forget spare tyre, remember to refit valve caps.'
    ),
    
    QData (
        'Tell me how you make sure your head restraint is correctly adjusted so it provides the best protection in the event of a crash.',
        'The head restraint should be adjusted so the rigid part of the head restraint is at least as high as the eye or top of the ears, and as close to the back of the head as is comfortable. Note: Some restraints might not be adjustable.'
    ),
    
    QData (
        'Tell me how you’d check the tyres to ensure that they have sufficient tread depth and that their general condition is safe to use on the road.',
        'No cuts and bulges, 1.6mm of tread depth across the central three-quarters of the breadth of the tyre, and around the entire outer circumference of the tyre.'
    ),
    
    QData (
        'Tell me how you’d check that the headlights and tail lights are working. You don’t need to exit the vehicle.',
        'Explain you’d operate the switch (turn on ignition if necessary), then walk round vehicle (as this is a ‘tell me’ question, you don’t need to physically check the lights).'
    ),
    
    QData (
        'Tell me how you’d know if there was a problem with your anti-lock braking system.',
        'Warning light should illuminate if there is a fault with the anti-lock braking system.'
    ),
    
    QData (
        'Tell me how you’d check the direction indicators are working. You don’t need to exit the vehicle.',
        'Explain you’d operate the switch (turn on ignition if necessary), and then walk round vehicle (as this is a ‘tell me’ question, you don’t need to physically check the lights).'
    ),
    
    QData (
        'Tell me how you’d check the brake lights are working on this car.',
        'Explain you’d operate the brake pedal, make use of reflections in windows or doors, or ask someone to help.'
    ),
    
    QData (
        'Tell me how you’d check the power-assisted steering is working before starting a journey.',
        'If the steering becomes heavy, the system may not be working properly. Before starting a journey, 2 simple checks can be made.\nGentle pressure on the steering wheel, maintained while the engine is started, should result in a slight but noticeable movement as the system begins to operate. Alternatively turning the steering wheel just after moving off will give an immediate indication that the power assistance is functioning.'
    ),
    
    QData (
        'Tell me how you’d switch on the rear fog light(s) and explain when you’d use it/them. You don’t need to exit the vehicle.',
        'Operate switch (turn on dipped headlights and ignition if necessary). Check warning light is on. Explain use.'
    ),
    
    QData (
        'Tell me how you switch your headlight from dipped to main beam and explain how you’d know the main beam is on.',
        'Operate switch (with ignition or engine on if necessary), check with main beam warning light.'
    ),
    
    QData (
        'Open the bonnet and tell me how you’d check that the engine has sufficient oil.',
        'Identify dipstick/oil level indicator, describe check of oil level against the minimum and maximum markers.'
    ),
    
    QData (
        'Open the bonnet and tell me how you’d check that the engine has sufficient engine coolant.',
        'Identify high and low level markings on header tank where fitted or radiator filler cap, and describe how to top up to correct level.'
    ),
    
    QData (
        'Open the bonnet and tell me how you’d check that you have a safe level of hydraulic brake fluid.',
        'Identify reservoir, check level against high and low markings.'
    ),
]

showme = [

    QData (
        'When it’s safe to do so, can you show me how you wash and clean the rear windscreen?'
    ),

    QData (
        'When it’s safe to do so, can you show me how you wash and clean the front windscreen?'
    ),

    QData (
        'When it’s safe to do so, can you show me how you’d switch on your dipped headlights?'
    ),

    QData (
        'When it’s safe to do so, can you show me how you’d set the rear demister?'
    ),

    QData (
        'When it’s safe to do so, can you show me how you’d operate the horn?'
    ),

    QData (
        'When it’s safe to do so, can you show me how you’d demist the front windscreen?'
    ),

    QData (
        'When it’s safe to do so, can you show me how you’d open and close the side window?'
    )
    
]