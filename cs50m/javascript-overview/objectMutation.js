const o = {
    a: 'siva',
    b: 'karthi',
    obj: {
        key: 'key',
    },
};

const o2 = Object.assign({}, o);

o2.obj.key = 'new-value';

console.log(o.obj.key);

// o2.a = 'new value';

// console.log(o2.a);
// console.log(o2.b);

// deep copy
function deepCopy(obj) {
    // check if vals are objects
    // if so, copy that object (deep copy)
    // else return the value
    const keys = Object.keys(obj);

    const newObject = {};

    for (let i = 0; i < keys.length; i++) {
        const key = keys[i];

        if (typeof obj[keys[i]] === 'object') {
            newObject[key] === deepCopy(obj[key])
        } else {
            newObject[key] = obj[key];
        }
        
    }
    return Object.assign({}, obj)
}

const o3 = deepCopy(o);

o.obj.key = 'new key!';
console.log(o3.obj.key);