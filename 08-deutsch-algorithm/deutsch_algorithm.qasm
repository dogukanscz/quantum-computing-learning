OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[1];
h q[0];
//phase kickback
x q[1];
h q[1];
barrier q[0], q[1];

//balanced oracle f(x) = x
cx q[0], q[1];
barrier q[0], q[1];

h q[0];
measure q[0] -> c[0];
