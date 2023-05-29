class ParkingSystem {
public:
    map<int, int> space;
    ParkingSystem(int big, int medium, int small) {
        space = {{1, big}, {2, medium}, {3, small}};
    }
    
    bool addCar(int carType) {
        return space[carType]-- > 0;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */
