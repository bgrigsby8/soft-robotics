# Module soft-robotics 

Soft Robotics is an industry-leading technology company that designs and builds automated AI-enabled solutions for inspection and robot picking applications using 3D machine vision, artificial intelligence and soft grippers.

## Model brad-grigsby:soft-robotics:coDrive

Gripper module to control the soft robotics coDrive vacuum controller.

### Configuration
The following attribute template can be used to configure this model:

```json
{
"d1_pin": <string>,
"d2_pin": <string>,
"d3_pin": <string>,
"board_name": <string>
}
```

#### Attributes

The following attributes are available for this model:

| Name          | Type   | Inclusion | Description                |
|---------------|--------|-----------|----------------------------|
| `d1_pin` | string  | Required  | Pin of D1 from coDrive |
| `d2_pin` | string | Required  | Pin of D2 from coDrive |
| `d3_pin` | string | Required | Pin of D3 from coDrive |
| `board_name` | string | Required | Name of board for GPIO connections |

#### Example Configuration

```json
{
  "d1_pin": "16",
  "d2_pin": "18",
  "d3_pin": "11",
  "board_name": "pi5"
}
```
