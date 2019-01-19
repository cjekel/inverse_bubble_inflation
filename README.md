# inverse_bubble_inflation
WIP: Identify material parameters from DIC bubble inflation tests...

# TODO DIC Test Data
- [x] Investigate different ways to store and compress numpy arrays
- [x] Create command line function that converts and stores DIC tec data into compressed arrays
- [x] Identify the specimen from test data 
- [x] Determine origin location for all tests (compare different methods for finding the origin)
- [ ] Open pressure data and find the the location where the pressure starts increasing
- [ ] Determine the location where the pressure stops increasing
- [ ] Create folders of the appropriate pressure data and corresponding npz of the displacement data
- [ ] Rotate option for certain tests
- [ ] Add circle adjust method
- [ ] Remove data points on bounds (if r > 95 mm, then remove)

# TODO FE Models
- [x] Identify appropriate abaqus material models (Appropriate models include hyperelastic fung orthotropic)
- [x] Plot material model response for uniaixal cases on 1 shell element
- [x] Determine reasonable shell/membrane formulation
- [x] Create bubble FE model
- [x] Export of displacement field data at specified locations
- [x] Specify the time increments to use to match the pressure data
- [x] Generate interpolation scheme for numerical model
- [ ] Formulate non-linear material model

# TODO Tie Everything together
- [ ] Objective function to calc difference between FE model and data
- [ ] Optimization strategy plan (perhaps EGO + SQP?)
- [ ] Complete inverse method 
