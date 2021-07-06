using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ECOMERCE.Models
{
    public partial class BookDBContext : DbContext
    {
        public BookDBContext()
        {

        }
        public BookDBContext(DbContextOptions<BookDBContext> options) : base(options)
        {


        }

        public virtual DbSet<Regalos> Regalos
        {
            get; set;
        }
    }
}
