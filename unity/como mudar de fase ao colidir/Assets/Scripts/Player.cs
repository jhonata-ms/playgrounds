using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    public float speedMovement;
    public float jumpForce;
    private Rigidbody2D rig;

    // Start is called before the first frame update
    void Start()
    {
        rig = GetComponent<Rigidbody2D>();
    }

    // Update is called once per frame
    void Update()
    {
        Jump();
        Move();
    }

    void Jump()
    {
        if(Input.GetButtonDown("Jump"))
        {
            rig.AddForce(new Vector2(0, jumpForce), ForceMode2D.Impulse);
        }
    }

    void Move()
    {
        Vector3 movement = new Vector3(Input.GetAxis("Horizontal"), 0, 0);
        transform.position += movement * Time.deltaTime * speedMovement;
    }
}
