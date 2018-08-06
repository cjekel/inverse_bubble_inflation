# inverse_bubble_inflation
WIP: Identify material paramters from DIC bubble inflation tests...

# TODO DIC Test Data
- [x] Investigate different ways to store and compress numpy arrays
- [x] Create command line function that converts and stores DIC tec data into compressed arrays
- [x] Identify the specimen from test data 
- [x] Determine origin location for all tests (compare different methods for fidning the origin)
- [ ] Open pressure data and find the the location where the pressure starts increassing
- [ ] Determine the location where the pressure stops increasing
- [ ] Create folders of the appropriate pressure data and corresponding npz of the displacement data

# TODO FE Models
- [x] Identify appropriate abaqus material models (Appropriate models include hyperelastic fung orthotropic)
- [x] Plot material model response for uniaixal cases on 1 shell element
- [ ] Determine reasonable shell/membrane formulation
- [ ] Create bubble FE model
- [ ] Export of displacement field data at specified locations
- [ ] Specify the time increments to use to match the pressure data

# TODO Tie Everything together
- [ ] Complete invesre method 
