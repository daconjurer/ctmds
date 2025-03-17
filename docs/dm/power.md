The price generation for power is based on the following concepts:

- power generation stack
- merit order principle
- marginal cost pricing model

### Power generation stack

The stack is modelled in the [stack module](../../ctmds/domain/commodity_price/commodities/electricity/generation_stack/stack.py)
and is an ordered sequence of power generators with a given maximum capacity.

### Merit order principle

Generators are selected from the cheapest to the most expensive. This emulates how
the power generation options are selected in real-world stacks.

### Marginal cost pricing model

The power price for a given data point is determined by the generator involved in the power
supply with the highest cost, whatever the demand it covers is.

## A simplified example

For example, for a demand of 25 GW at 7:00 AM, if the stack is as follows:

- Renewables:
    - Wind
        - Maximum capacity: 14.5 GW
        - Marginal cost: £5
    - Solar
        - Maximum capacity: 2 GW
        - Marginal cost: £2
- Fossil fuels:
    - Gas
        - Maximum capacity: 15 GW
        - Marginal cost: £15
- Other sources:
    - Nuclear
        - Maximum capacity: 4 GW
        - Marginal cost: £8
    - Peaking plants (random):
        - Maximum capacity: 10 GW
        - Marginal cost: £30

Now, the demand can be satisfied as follows using the merit order principle:

```
- Solar: 2 GW / 25 GW = 8%          | Total generated: 2 GW     (8%)
- Wind: 14.5 GW / 25 GW = 58%       | Total generated: 16.5 GW  (66%)
- Nuclear: 4 GW / 25 GW = 16%       | Total generated: 20.5 GW  (82%)
- Gas: 4.5 GW / 25 GW = 18%         | Total generated: 25 GW    (100%)
```

This means that for this data point, the simplified price would be £15 if we
follow the marginal cost pricing model, as gas is involved in the supply of the
power demand.
