# MeshBaker
Interface to communicate across multiple baking packages

# Usage

## config.json
> Path to baking application

## export_setting.json
> data to feed baking application

## crossbaker.exportSettings
> Contain all setting to export with

## crossbaker.bakers
> Contain all available baker found in system
    > cross.bakers.run() : run current baker specified in crossbaker.exportSettings\

​```flow
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end

st->op->cond
cond(yes)->e
cond(no)->op
​```