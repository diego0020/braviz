# Braviz Messages

## Subject

Communicate a change of the current focus subject

### Syntax:

```javascript
{
type : "subject",
subject : <subj_id>
}
```

## Sample

Communicate a change in the current focus sample

### Syntax

For all processes
```javascript
{
type : "sample",
sample : <subjects list>
}
```

For a single process
```javascript
{
type : "sample",
sample : <subjects list>,
target : <id_of target instance>
}
```

## Log

Communicate data about user actions. Include application state (scenario), so that the state can be revisited.

### Syntax

```javascript
{
type : "log",
action: <description of user action>,
state : <resulting state of the application>,
pid : <id of application instance>,
application :  <name of application>,
time : timestamp when the action happened,
sceensshot : <optional,  base64 encoded raw png data of a 128x128 image>
}
```

Example

```javascript
{
type: "log",
action: subject changed,
state : {current_subject: 10, variables: [45, 14,32], plot: ['scatter']},
pid : 1546,
application : 'anova',
time : 105130014
}
```

## Reload State

Used to reload the state of an application stored in the log db. 

If the application that created that state is still open:

    -   Should it be reloaded on the same instance? (the current implementation will do this,
        but it has to be discussed with users).
    -   or should a new instance be launched?
    
If the application is no longer available then the menu should spawn a new instance, and then wait for the ready message
from it. After that the menu will send the message again with the target changed to the new instance.

### Syntax

```javascript
{
type : "reload",
target : <instance_id>,
scenario : <scenario data>
}
```

### Example

```javascript
{
type : "reload",
target : '486f3202-2d12-4122-9ad3-69c884c8ccbd',
scenario : {outcome : "my_outcome", sample : [1,2,3,4], regressors:["reg_1". "reg_2"]}
}
```

## Variables

Used to suggest variables from one application to the others. Applications that receive the message
should display a dialog indicating the suggestion and asking the user if he wants to add all of them 
or a subset to the working set of variables.

### Syntax

```javascript
{
type : "variables",
variables : <vars_list>
}
```


### Example

```javascript
{
type : "variables",
variables : ["var_1", "var_2", "var_3"]
}
```

## Visualization

These messages are used to share visualizations between applications. The punctual cases considered right now are

    - Copy the configuration of one subject_overview application to another, useful for comparing subjects side by side
    - Copy the configuration fron one subject_overview application to a sample_overview without saving a scenario

These messages should be targeted to a specific application instance in order to not affect the state of other applications.
For this purpose the sender instance must know which receivers are available and ask the user to select one of them. 

In the future more cases may be added.

### Syntax

```javascript
{
type : "Visualization",
source : "subject_overview",
target : <id_of_target_application>,
scenario : <scenario_data>
}
```

### Example

```javascript
{
type : "Visualization",
source : "subject_overview",
scenario : <scenario_data>
}
```

## Ready

### Syntax

```javascript
{
type : "ready",
source_pid : <pid>,
source_id : <uid>
}
```

### Example

Desktop application

```javascript
{
type : "ready",
source_pid : 345,
source_id : '486f3202-2d12-4122-9ad3-69c884c8ccbd'
}
```

Web application

```javascript
{
type : "ready",
source_pid : 345,
source_id : '486f3202-2d12-4122-9ad3-69c884c8ccbd'
}
```