const o = new Object();
o.firstName = "siva"
o.lastName = "karthi"
o.isTeaching = true
o.greet = function() {
    console.log('hi!')
}

const o2 = {}
o2.firstName = "siva"
o2['lastName'] = "karthi"
const key = "isTeaching"
o[key] = true
o['greet'] = function() {
    console.log('hi!')
}

const o3 = {
    firstName: "siva",
    lastName: "karthi",
    isTeaching: true,
    greet: function() {
        console.log('hi!');
    },
    address: {
        number: 123,
        street: "Main Street"
    }
}