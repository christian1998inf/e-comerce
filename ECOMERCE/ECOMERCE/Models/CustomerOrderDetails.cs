﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace ECOMERCE.Models
{
    public class CustomerOrderDetails
    {
        public int OrderDetailsId { get; set; }

        public string OrderId { get; set; }

        public int ProductId { get; set; }

        public int Quantity { get; set; }

        public decimal Price { get; set; }



    }
}
