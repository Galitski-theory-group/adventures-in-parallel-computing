from random import randint

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

LOWER_LIMIT = 1
UPPER_LIMIT = 10

status = MPI.Status()

if rank != 0:
    data = randint(LOWER_LIMIT, UPPER_LIMIT)
    comm.send(data, dest=0, tag=1)
else:
    for r in range(1, size):
        data = comm.recv(source=r, status=status)
        print(f"my name is rank 0 and I received the number {data} from rank {r}")
        print(
            f"The status object : \n source: {status.source} \n tag: {status.tag} \n \
byte_count : {status.count}"
        )
